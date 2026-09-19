# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pb
%define go_import_path  github.com/cheggaaa/pb/v3

Name:           go-github-cheggaaa-pb-v3
Version:        3.1.7
Release:        %autorelease
Summary:        Terminal progress bars for Go v3
License:        BSD-3-Clause
URL:            https://github.com/cheggaaa/pb
#!RemoteAsset:  sha256:2545c01a291a1d8cafa44b0e5865498c71a5bed18f291d46bdf0851a52018141
Source0:        https://github.com/cheggaaa/pb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/VividCortex/ewma)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/cheggaaa/pb/v3) = %{version}

Requires:       go(github.com/VividCortex/ewma)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(golang.org/x/sys)

%description
Progress bars for Go applications with customizable templates,
multiple-bar pools and transfer-rate tracking. This package provides the v3 API.

%prep -a
# The v3 module lives below the repository root.
cp README.md v3/
find . -maxdepth 1 -mindepth 1 ! -name v3 -exec rm -rf {} +
mv v3/* .
rmdir v3

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
