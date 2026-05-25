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
Summary:        A go implementation of metrics reporting for Circonus
License:        BSD-3-Clause
URL:            https://github.com/circonus-labs/circonus-gometrics
#!RemoteAsset:  sha256:23ab14e6b4db910c15ab2dc23b1cab7b54ba1ec2dd1082eb7763bbe9b6d64171
Source0:        https://github.com/circonus-labs/circonus-gometrics/archive/refs/tags/v1.2.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-go-retryablehttp-checkretry-signature.patch

BuildOption(prep):  -n circonus-gometrics-1.2.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/circonus-labs/circonusllhist)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)

Provides:       go(github.com/circonus-labs/circonus-gometrics) = %{version}
Provides:       go(github.com/circonus-labs/circonus-gometrics/api) = %{version}
Provides:       go(github.com/circonus-labs/circonus-gometrics/api/config) = %{version}
Provides:       go(github.com/circonus-labs/circonus-gometrics/checkmgr) = %{version}

Requires:       go(github.com/circonus-labs/circonusllhist)
Requires:       go(github.com/hashicorp/go-retryablehttp)


%description
Circonus metrics tracking for Go applications

This library supports named counters, gauges and histograms. It also
provides convenience wrappers for registering latency instrumented
functions with Go's builtin http server.

Initializing only requires setting an API Token
(https://login.circonus.com/user/tokens) at a minimum.

Options


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
