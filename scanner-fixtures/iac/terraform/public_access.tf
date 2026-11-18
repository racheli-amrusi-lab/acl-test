# Intentionally insecure Terraform fixture.
# Scanner testing only: do not apply.
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "public_logs" {
  bucket = "scanner-fixture-public-logs"
}

resource "aws_s3_bucket_public_access_block" "public_logs" {
  bucket                  = aws_s3_bucket.public_logs.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_security_group" "open_ssh" {
  name = "scanner-fixture-open-ssh"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
