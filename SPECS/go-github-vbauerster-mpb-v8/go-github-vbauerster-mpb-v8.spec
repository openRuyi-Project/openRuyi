# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mpb
%define go_import_path  github.com/vbauerster/mpb/v8

Name:           go-github-vbauerster-mpb-v8
Version:        8.9.3
Release:        %autorelease
Summary:        Multi progress bars for terminal applications
License:        Unlicense
URL:            https://github.com/vbauerster/mpb
#!RemoteAsset:  sha256:36f93a4919f8f99e05751d96ebe66291c36f74b18a2706dac9f16f5a1ac5b465
Source0:        https://github.com/vbauerster/mpb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/VividCortex/ewma)
BuildRequires:  go(github.com/acarl005/stripansi)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/vbauerster/mpb/v8) = %{version}

Requires:       go(github.com/VividCortex/ewma)
Requires:       go(github.com/acarl005/stripansi)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(golang.org/x/sys)

%description
mpb/v8 renders one or more progress bars in terminal applications, with
decorators for ETA, percentage, and byte counters.

%prep -a
# _examples are sample programs. _svg holds README images.
rm -rf _examples _svg

%files
%doc README.md
%license UNLICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
