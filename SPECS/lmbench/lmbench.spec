# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global full_version 3.0-a9

Name:           lmbench
Version:        3.0_a9
Release:        %autorelease
Summary:        Utilities to benchmark UNIX systems
License:        GPL with additional restrictions
URL:            https://sourceforge.net/projects/lmbench
# VCS: No VCS link available
#!RemoteAsset:  sha256:cbd5777d15f44eab7666dcac418054c3c09df99826961a397d9acf43d8a2a551
Source0:        https://sourceforge.net/projects/lmbench/files/development/lmbench-%{full_version}/lmbench-%{full_version}.tgz
Source1:        lmbench
BuildSystem:    autotools

# Modernize K&R C code to ANSI C prototypes and link libtirpc to fix build errors
Patch2000:      2000-Fix-build-errors.patch
# Change default mail setting from "yes" to "no"
Patch2001:      2001-set-no-mail.patch

BuildRequires:  libtirpc-devel

Requires:       perl
Requires:       make

%description
Lmbench is a set of utilities to test the performance of a unix system
producing detailed results as well as providing tools to process them.
It includes a series of micro benchmarks that measure some basic operating
system and hardware metrics:
* file reading and summing
* memory bandwidth while reading, writing and copying
* copying data through pipes
* copying data through Unix sockets
* reading data through TCP/IP sockets

%conf
# No conf

%install
# Use our own install step
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/lmbench
install -Dp -m0644 results/Makefile %{buildroot}%{_prefix}/lib/lmbench/results/Makefile
install -Dp -m0644 src/webpage-lm.tar %{buildroot}%{_prefix}/lib/lmbench/src/webpage-lm.tar
cp -avx bin/ scripts/ %{buildroot}%{_prefix}/lib/lmbench/
find %{buildroot}%{_prefix}/lib/lmbench/ -name '*.[ao]' -exec %{__rm} -f {} \;
chmod a-x %{buildroot}%{_prefix}/lib/lmbench/scripts/info-template

%check
# no tests

%files
%doc ACKNOWLEDGEMENTS CHANGES hbench-REBUTTAL README doc
%license COPYING COPYING-2
%{_bindir}/lmbench
%{_prefix}/lib/lmbench/

%changelog
%autochangelog
