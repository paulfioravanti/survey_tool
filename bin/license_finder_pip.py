#!/usr/bin/env ruby
# frozen_string_literal: true

# This file was generated by Bundler.
#
# The application 'license_finder_pip.py' is installed as part of a gem, and
# this file is here to facilitate running it.

require "pathname"
ENV["BUNDLE_GEMFILE"] ||=
  File.expand_path("../../Gemfile", Pathname.new(__FILE__).realpath)

require "rubygems"
require "bundler/setup"

load Gem.bin_path("license_finder", "license_finder_pip.py")
