# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gohistogram
%define go_import_path  github.com/VividCortex/gohistogram

Name:           go-github-vividcortex-gohistogram
Version:        1.0.0
Release:        %autorelease
Summary:        Weighted and exponential histograms for Go
License:        MIT
URL:            https://github.com/VividCortex/gohistogram
#!RemoteAsset:  sha256:830abe53f98e7a46ccbd829114998e1d7bbe9edfeb669011e7970d684493809e
Source0:        https://github.com/VividCortex/gohistogram/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Package gohistogram provides weighted and exponential histogram
implementations for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
