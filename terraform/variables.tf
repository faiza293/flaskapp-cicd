variable "project" {
  description = "The Google Cloud project ID"
}

variable "region" {
  description = "The region to deploy resources in"
  default     = "us-central1"
}

variable "zone" {
  description = "The zone to deploy resources in"
  default     = "us-central1-a"
}
