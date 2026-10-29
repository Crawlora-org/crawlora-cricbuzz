require_relative "lib/crawlora/cricbuzz/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-cricbuzz"
  spec.version = Crawlora::Cricbuzz::VERSION
  spec.summary = "Cricbuzz API client for Crawlora (29 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Cricbuzz API. Covers cricket matches, schedules, news, rankings, series, and records across 29 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-cricbuzz", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
