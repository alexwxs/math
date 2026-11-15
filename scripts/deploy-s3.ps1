# Deploy the static site (public/) to an S3 website bucket.
# Prerequisites: AWS CLI installed and configured (`aws configure`).
#
# Usage:
#   .\scripts\deploy-s3.ps1 -Bucket my-math-site -Region ap-southeast-2
#   .\scripts\deploy-s3.ps1 -Bucket my-math-site -Region ap-southeast-2 -Create

param(
  [Parameter(Mandatory = $true)][string]$Bucket,
  [string]$Region = "ap-southeast-2",
  [switch]$Create
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Public = Join-Path $Root "public"

if (-not (Get-Command aws -ErrorAction SilentlyContinue)) {
  throw "AWS CLI not found. Install from https://aws.amazon.com/cli/ then run: aws configure"
}

if ($Create) {
  Write-Host "Creating bucket s3://$Bucket in $Region ..."
  if ($Region -eq "us-east-1") {
    aws s3api create-bucket --bucket $Bucket --region $Region | Out-Null
  } else {
    aws s3api create-bucket --bucket $Bucket --region $Region `
      --create-bucket-configuration "LocationConstraint=$Region" | Out-Null
  }

  aws s3api put-public-access-block --bucket $Bucket --public-access-block-configuration `
    "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

  $policy = @"
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::$Bucket/*"
  }]
}
"@
  $policyPath = Join-Path $env:TEMP "math-s3-policy.json"
  Set-Content -Path $policyPath -Value $policy -Encoding utf8
  aws s3api put-bucket-policy --bucket $Bucket --policy "file://$policyPath"

  aws s3api put-bucket-website --bucket $Bucket --website-configuration `
    '{\"IndexDocument\":{\"Suffix\":\"index.html\"},\"ErrorDocument\":{\"Key\":\"index.html\"}}'
}

Write-Host "Syncing $Public -> s3://$Bucket ..."
aws s3 sync $Public "s3://$Bucket" --delete --region $Region `
  --cache-control "max-age=300" `
  --exclude "*.html" 
aws s3 sync $Public "s3://$Bucket" --region $Region `
  --exclude "*" --include "*.html" --cache-control "no-cache"

$website = "http://$Bucket.s3-website-$Region.amazonaws.com"
if ($Region -eq "us-east-1") {
  $website = "http://$Bucket.s3-website-us-east-1.amazonaws.com"
}
Write-Host "Done. Site URL: $website"
