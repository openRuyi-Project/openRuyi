# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gawk
Version:        5.4.0
Release:        %autorelease
Summary:        Domain-specific language for text processing
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gawk/
VCS:            git:https://https.git.savannah.gnu.org/git/gawk.git
#!RemoteAsset:  sha256:3dd430f0cd3b4428c6c3f6afc021b9cd3c1f8c93f7a688dc268ca428a90b4ac1
Source:         http://ftpmirror.gnu.org/gnu/gawk/gawk-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  pkgconfig(mpfr)

Provides:       awk
Provides:       /bin/gawk

%description
AWK is a domain-specific language designed for text processing and
typically used as a data extraction and reporting tool.

GNU awk is upwardly compatible with the System V Release 4 awk.  It is
almost completely POSIX 1003.2 compliant.

%install -a
%find_lang %{name} --generate-subpackages

%files
%config %{_sysconfdir}/profile.d/gawk.csh
%config %{_sysconfdir}/profile.d/gawk.sh
%{_bindir}/awk
%license COPYING*
%doc AUTHORS NEWS POSIX.STD README ChangeLog*
%{_bindir}/gawk*
%{_libexecdir}/awk
%{_libdir}/gawk
%{_datadir}/awk
%{_includedir}/gawkapi.h
%{_infodir}/*.info*
%{_infodir}/gawk_*
%{_mandir}/man1/gawk.1*
%{_mandir}/man1/gawkbug.1*
%{_mandir}/man1/pm-gawk.1*
%{_mandir}/man3/*

%changelog
%autochangelog
