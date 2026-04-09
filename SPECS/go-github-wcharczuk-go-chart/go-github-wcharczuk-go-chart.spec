# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-chart
%define go_import_path  github.com/wcharczuk/go-chart

Name:           go-github-wcharczuk-go-chart
Version:        2.1.2
Release:        %autorelease
Summary:        go chart is a basic charting library in go.
License:        MIT
URL:            https://github.com/wcharczuk/go-chart
#!RemoteAsset
Source0:        https://github.com/wcharczuk/go-chart/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BUildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(golang.org/x/image)

Provides:       go(github.com/wcharczuk/go-chart) = %{version}

%description
Package `chart` is a very simple golang native charting library that supports timeseries and continuous line charts.

Master should now be on the v3.x codebase, which overhauls the api significantly. Per usual, see `examples` for more information.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
