# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           colorprofile
%define go_import_path  github.com/charmbracelet/colorprofile

Name:           go-github-charmbracelet-colorprofile
Version:        0.4.2
Release:        %autorelease
Summary:        Magical terminal color handling 🪄
License:        MIT
URL:            https://github.com/charmbracelet/colorprofile
#!RemoteAsset
Source0:        https://github.com/charmbracelet/colorprofile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/charmbracelet/x)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/charmbracelet/colorprofile) = %{version}

Requires:       go(github.com/charmbracelet/x)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/xo/terminfo)

%description
A simple, powerful—and at times magical—package for detecting terminal
color profiles and performing color (and CSI) degradation.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
