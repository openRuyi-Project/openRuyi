# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ewma
%define go_import_path  github.com/VividCortex/ewma

Name:           go-github-vividcortex-ewma
Version:        1.2.0
Release:        %autorelease
Summary:        Exponentially weighted moving averages for Go
License:        MIT
URL:            https://github.com/VividCortex/ewma
#!RemoteAsset:  sha256:2f26521a9207b91dfbca3d28e5545bc11cb098888ecf3e9ba8e5936387b06a33
Source0:        https://github.com/VividCortex/ewma/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/VividCortex/ewma) = %{version}

%description
ewma implements exponentially weighted moving averages, used by the
mpb progress-bar library.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
