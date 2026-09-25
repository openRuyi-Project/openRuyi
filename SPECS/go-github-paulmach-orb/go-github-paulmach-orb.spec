# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           orb
%define go_import_path  github.com/paulmach/orb

Name:           go-github-paulmach-orb
Version:        0.13.0
Release:        %autorelease
Summary:        Geometry types and algorithms for Go
License:        MIT
URL:            https://github.com/paulmach/orb
#!RemoteAsset:  sha256:8c8b6113607ad8de427e33cecc687ac98d619b09ede8c6674d79d7a363484313
Source0:        https://github.com/paulmach/orb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/paulmach/protoscan)
BuildRequires:  go(go.mongodb.org/mongo-driver/v2)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/paulmach/protoscan)
Requires:       go(go.mongodb.org/mongo-driver/v2)

%description
Orb provides geometry types, spatial algorithms, GeoJSON handling, map tiles,
and binary or text geometry encodings for Go applications.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
