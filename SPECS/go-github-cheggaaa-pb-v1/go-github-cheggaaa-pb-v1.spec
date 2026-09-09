# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pb
%define go_import_path  github.com/cheggaaa/pb
%define ver_v3          3.1.7

Name:           go-github-cheggaaa-pb-v1
Version:        1.0.29
Release:        %autorelease
Summary:        Console progress bar for Golang
License:        BSD-3-Clause
URL:            https://github.com/cheggaaa/pb
#!RemoteAsset:  sha256:73090c024e062216207ccd7a3339da3d1f87396abccd3271ed26e42c7d487eb2
Source0:        https://github.com/cheggaaa/pb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:2545c01a291a1d8cafa44b0e5865498c71a5bed18f291d46bdf0851a52018141
Source1:        https://github.com/cheggaaa/pb/archive/v%{ver_v3}.tar.gz#/%{_name}-v3-%{ver_v3}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/VividCortex/ewma)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/cheggaaa/pb) = %{version}
Provides:       go(github.com/cheggaaa/pb/v3) = %{ver_v3}

Requires:       go(github.com/VividCortex/ewma)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(golang.org/x/sys)

%description
Terminal progress bars for Go. The existing root API and the independently
versioned v3 module are installed together from their respective tags.

%prep -a
# Keep the root module at its existing version and replace only the v3 subtree.
mkdir .pb-v3
%{__tar} -xf %{SOURCE1} --strip-components=1 -C .pb-v3
rm -rf v3
mv .pb-v3/v3 v3
rm -rf .pb-v3

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
