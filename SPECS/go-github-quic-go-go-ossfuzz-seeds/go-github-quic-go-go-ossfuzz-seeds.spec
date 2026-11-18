# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ossfuzz-seeds
%define go_import_path  github.com/quic-go/go-ossfuzz-seeds
# Skip nested testing subpackage requiring unpackaged go-118-fuzz-build.
%define go_test_exclude github.com/quic-go/go-ossfuzz-seeds/testing

Name:           go-github-quic-go-go-ossfuzz-seeds
Version:        0.1.0
Release:        %autorelease
Summary:        Writes Go native fuzz seeds as OSS-Fuzz seed corpus files
License:        MIT
URL:            https://github.com/quic-go/go-ossfuzz-seeds
#!RemoteAsset:  sha256:4339d0aa70d4949c2e8f79b9bba958ebc0b21551b0e42d4652557f4a3fe427a8
Source0:        https://github.com/quic-go/go-ossfuzz-seeds/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/quic-go/go-ossfuzz-seeds) = %{version}

%description
Wraps testing.F to write Go native fuzzing seeds as OSS-Fuzz seed corpus files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
