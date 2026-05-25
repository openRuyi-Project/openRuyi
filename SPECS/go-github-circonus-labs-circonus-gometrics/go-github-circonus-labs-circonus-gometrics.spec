# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           circonus-gometrics
%define go_import_path  github.com/circonus-labs/circonus-gometrics

Name:           go-github-circonus-labs-circonus-gometrics
Version:        1.2.0
Release:        %autorelease
Summary:        Metrics reporting implementation for Circonus
License:        BSD-3-Clause
URL:            https://github.com/circonus-labs/circonus-gometrics
#!RemoteAsset:  sha256:23ab14e6b4db910c15ab2dc23b1cab7b54ba1ec2dd1082eb7763bbe9b6d64171
Source0:        https://github.com/circonus-labs/circonus-gometrics/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Adapt only internal retryablehttp callback literals to the packaged
# go-retryablehttp v0.7.8 API. No exported circonus-gometrics API changes;
# retry behavior is unchanged because the new ctx/logger args are unused.
# Test changes only relax Go-version-sensitive error strings. - HNO3Miracle
Patch2000:      2000-fix-go-retryablehttp-checkretry-signature.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/circonus-labs/circonusllhist)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)

Provides:       go(github.com/circonus-labs/circonus-gometrics) = %{version}

Requires:       go(github.com/circonus-labs/circonusllhist)
Requires:       go(github.com/hashicorp/go-retryablehttp)

%description
This library supports named counters, gauges, and histograms. It also
provides wrappers for registering latency-instrumented functions with
Go's built-in HTTP server.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
