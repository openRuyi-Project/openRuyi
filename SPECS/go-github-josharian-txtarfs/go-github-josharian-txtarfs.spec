# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           txtarfs
%define go_import_path  github.com/josharian/txtarfs

Name:           go-github-josharian-txtarfs
Version:        0+git20261030.5dc76b8
Release:        %autorelease
Summary:        Convert txtar archives to fs.FS values
License:        MIT
URL:            https://github.com/josharian/txtarfs
#!RemoteAsset:  sha256:1920393838fcb1332fae4ac61a1dfc350324a684bc5f845e2d67405725603a66
Source0:        https://github.com/josharian/txtarfs/archive/5dc76b8fe6bf.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/josharian/mapfs)
BuildRequires:  go(golang.org/x/tools/txtar)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/cmd/txtar) = %{version}

Requires:       go(github.com/josharian/mapfs)
Requires:       go(golang.org/x/tools/txtar)

%description
txtarfs converts between txtar archives and fs.FS values.

%files
%doc readme.md
%license license
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
