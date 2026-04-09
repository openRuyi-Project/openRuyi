# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           busybox
Version:        1.37.0
Release:        %autorelease
Summary:        Minimalist variant of UNIX utilities linked in a single executable
License:        GPL-2.0-or-later
URL:            https://www.busybox.net/
# VCS: No reliable VCS link available
#!RemoteAsset
Source0:        https://busybox.net/downloads/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source1:        https://busybox.net/downloads/%{name}-%{version}.tar.bz2.sig
BuildSystem:    autotools

# Disables CBQ-related help/output in BusyBox tc
Patch0:         busybox-1.36.1-no-cbq.patch
# Restricts the SHA-NI SHA1 fast-path check to GCC x86/x86_64
Patch1:         busybox-1.37.0-fix-conditional-for-sha1_process_block64_shaNI.patch

BuildOption(check):  SKIP_KNOWN_BUGS=1
BuildOption(check):  SKIP_INTERNET_TESTS=1

# Tests related
BuildRequires:  zip
BuildRequires:  hostname

%description
BusyBox combines tiny versions of many common UNIX utilities into a
single executable. It provides minimalist replacements for utilities
usually found in fileutils, shellutils, findutils, textutils, grep,
gzip, tar, and more. BusyBox provides a fairly complete POSIX
environment for small or embedded systems. The utilities in BusyBox
generally have fewer options than their GNU cousins. The options that
are included provide the expected functionality and behave much like
their GNU counterparts.
BusyBox is for emergency and special use cases. Replacing the standard
tools in a system is not supported. Some tools don't work out of the
box but need special configuration, like udhcpc, the dhcp client.

%conf # BusyBox has no configuration script.

%build -p
make defconfig # Create the maximum "sane" configuration.

%install # BusyBox needs to be installed manually.
         # Arch Linux for reference.
install -Dm0755 busybox %{buildroot}%{_bindir}/busybox
install -Dm644 docs/busybox.1 %{buildroot}%{_mandir}/man1/busybox.1

%check -p
# This test might not fit OBS environment.
rm -f testsuite/taskset.tests

%files
%license LICENSE
%doc README examples
%{_bindir}/busybox
%{_mandir}/man1/busybox.*

%changelog
%autochangelog
