# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-pinyin
%define go_import_path  github.com/mozillazg/go-pinyin

Name:           go-github-mozillazg-go-pinyin
Version:        0.19.0
Release:        %autorelease
Summary:        Chinese character to pinyin conversion library for Go
License:        MIT
URL:            https://github.com/mozillazg/go-pinyin
#!RemoteAsset:  sha256:edabc78f13356ed742c5ac7b46eb23fc04d74a06e321075aeba40c7affe2fdab
Source0:        https://github.com/mozillazg/go-pinyin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-isatty)

Provides:       go(github.com/mozillazg/go-pinyin) = %{version}

Requires:       go(github.com/mattn/go-isatty)

%description
This library converts Chinese characters to pinyin, with support for
tone styles, heteronyms and custom pronunciation dictionaries.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
