# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godot
%define go_import_path  github.com/tetafro/godot

Name:           go-github-tetafro-godot
Version:        1.5.6
Release:        %autorelease
Summary:        Checks if comments contain a period at the end of the last sentence if needed
License:        MIT
URL:            https://github.com/tetafro/godot
#!RemoteAsset:  sha256:3f8c29ee7da8b930386187106f59fc392f52e25d0269cf5a4ab56cfb48c636eb
Source0:        https://github.com/tetafro/godot/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/tetafro/godot) = %{version}

Requires:       go(go.yaml.in/yaml/v3)

%description
Checks if comments contain a period at the end of the last sentence if needed.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n godot-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/tetafro/godot

%changelog
%autochangelog
