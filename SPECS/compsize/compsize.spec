# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           compsize
Version:        1.5
Release:        %autorelease
Summary:        Utility for measuring compression ratio of files on btrfs
License:        GPL-2.0-or-later
URL:            https://github.com/kilobyte/compsize
#!RemoteAsset
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/kilobyte/compsize/pull/54
Patch0:         compsize-1.5-fix-build-btrfsprogs-0.6.1.patch
BuildSystem:    autotools

BuildRequires:  btrfs-progs-devel
BuildRequires:  make

%description
compsize takes a list of files (given as arguments) on a btrfs
filesystem and measures used compression types and effective
compression ratio, producing a report.

# No configure script in this project
%conf

# No check
%check

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc README.md
%license LICENSE
%{_bindir}/compsize
%{_mandir}/man8/compsize.8%{?ext_man}

%changelog
%autochangelog
