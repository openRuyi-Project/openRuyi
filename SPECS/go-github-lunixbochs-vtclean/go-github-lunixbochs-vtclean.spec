# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vtclean
%define go_import_path  github.com/lunixbochs/vtclean

Name:           go-github-lunixbochs-vtclean
Version:        1.0.0
Release:        %autorelease
Summary:        strips terminal escapes from text, can preserve color
License:        MIT
URL:            https://github.com/lunixbochs/vtclean
#!RemoteAsset:  sha256:38aa5c60284f77cbb4be1de4af8907ce66954ff1a11e4f910d02e0283ce13b33
Source0:        https://github.com/lunixbochs/vtclean/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lunixbochs/vtclean) = %{version}

%description
Clean up raw terminal output by stripping escape sequences, optionally
preserving color.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
