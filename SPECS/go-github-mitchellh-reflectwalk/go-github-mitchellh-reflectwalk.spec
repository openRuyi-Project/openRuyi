# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reflectwalk
%define go_import_path  github.com/mitchellh/reflectwalk

Name:           go-github-mitchellh-reflectwalk
Version:        1.0.2
Release:        %autorelease
Summary:        reflectwalk is a Go library for "walking" complex structures, similar to walking a filesystem.
License:        MIT
URL:            https://github.com/mitchellh/reflectwalk
#!RemoteAsset
Source0:        https://github.com/mitchellh/reflectwalk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/reflectwalk) = %{version}

%description
reflectwalk is a Go library for "walking" a value in Go using
reflection, in the same way a directory tree can be "walked" on the
filesystem. Walking a complex structure can allow you to do
manipulations on unknown structures such as those decoded from JSON.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
