# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gamut
%define go_import_path  github.com/muesli/gamut

Name:           go-github-muesli-gamut
Version:        0.3.1
Release:        %autorelease
Summary:        Go package to generate and manage color palettes & schemes 🎨
License:        MIT
URL:            https://github.com/muesli/gamut
#!RemoteAsset
Source0:        https://github.com/muesli/gamut/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/muesli/clusters)
BuildRequires:  go(github.com/muesli/kmeans)
BuildRequires:  go(github.com/xrash/smetrics)

Provides:       go(github.com/muesli/gamut) = %{version}

Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/muesli/clusters)
Requires:       go(github.com/muesli/kmeans)
Requires:       go(github.com/xrash/smetrics)

%description
gamut operates on various color spaces internally, but all color values
you pass in as parameters and all return values will match Go’s
color.Color interface.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
