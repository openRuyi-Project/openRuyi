# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           emoji
%define go_import_path  github.com/kyokomi/emoji/v2

Name:           go-github-kyokomi-emoji-v2
Version:        2.2.13
Release:        %autorelease
Summary:        :sushi: emoji terminal output for golang
License:        MIT
URL:            https://github.com/kyokomi/emoji
#!RemoteAsset:  sha256:abc1e097e6831fc7957710611c59ee34ee26378ab3a0cbbc9172435ba71279f0
Source0:        https://github.com/kyokomi/emoji/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kyokomi/emoji/v2) = %{version}

%description
emoji provides emoji support for Go, turning :emoji: aliases into their Unicode characters.

# cmd/ is a code generator pulling goquery; not needed by the library.
%prep -a
rm -rf cmd

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
