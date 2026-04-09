# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ansi
%define go_import_path  github.com/muesli/ansi
%define commit_id 276c6243b2f6df61db727937762b1a3f9cc12486

Name:           go-github-muesli-ansi
Version:        0+git20230316.276c624
Release:        %autorelease
Summary:        Raw ANSI sequence helpers
License:        MIT
URL:            https://github.com/muesli/ansi
#!RemoteAsset
Source0:        https://github.com/muesli/ansi/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/muesli/ansi) = %{version}

Requires:       go(github.com/mattn/go-runewidth)

%description
Raw ANSI sequence helpers

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
