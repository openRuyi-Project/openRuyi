# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-archive
%define go_import_path  github.com/moby/go-archive

Name:           go-github-moby-go-archive
Version:        0.3.3
Release:        %autorelease
Summary:        Archive handling utilities from Moby
License:        Apache-2.0
URL:            https://github.com/moby/go-archive
#!RemoteAsset:  sha256:edb726704379d095bea244e3c55ee7f3abed67525cbf95f0e7a1ada4a9eb536c
Source0:        https://github.com/moby/go-archive/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/AdaLogics/go-fuzz-headers)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/moby/patternmatcher)
BuildRequires:  go(github.com/moby/sys/mount)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/moby/sys/reexec)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gotest.tools/v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/containerd/log)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/moby/patternmatcher)
Requires:       go(github.com/moby/sys/mount)
Requires:       go(github.com/moby/sys/mountinfo)
Requires:       go(github.com/moby/sys/reexec)
Requires:       go(github.com/moby/sys/sequential)
Requires:       go(github.com/moby/sys/user)
Requires:       go(github.com/moby/sys/userns)
Requires:       go(golang.org/x/sys)

%description
Moby go-archive provides tar, compression, chroot extraction, and archive path
utilities used by container tooling.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
