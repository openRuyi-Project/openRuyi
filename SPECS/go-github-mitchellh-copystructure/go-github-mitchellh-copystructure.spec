# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           copystructure
%define go_import_path  github.com/mitchellh/copystructure

Name:           go-github-mitchellh-copystructure
Version:        1.2.0
Release:        %autorelease
Summary:        Go (golang) library for deep copying values in Go.
License:        MIT
URL:            https://github.com/mitchellh/copystructure
#!RemoteAsset
Source0:        https://github.com/mitchellh/copystructure/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mitchellh/reflectwalk)

Provides:       go(github.com/mitchellh/copystructure) = %{version}

Requires:       go(github.com/mitchellh/reflectwalk)

%description
copystructure is a Go library for deep copying values in Go.

This allows you to copy Go values that may contain reference values such
as maps, slices, or pointers, and copy their data as well instead of
just their references.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
