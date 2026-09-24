# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cvs
Version:        1.12.13
Release:        %autorelease
Summary:        Concurrent Versions System
License:        GPL-1.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Latex2e-translated-notice
URL:            https://www.nongnu.org/cvs/
VCS:            cvs::pserver:anonymous@cvs.savannah.nongnu.org:/sources/cvs
#!RemoteAsset:  sha256:78853613b9a6873a30e1cc2417f738c330e75f887afdaf7b3d0800cb19ca515e
Source:         https://ftp.gnu.org/non-gnu/cvs/source/feature/%{version}/cvs-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  procps-ng
BuildRequires:  rsync

Requires:       %{_bindir}/ssh
Requires:       %{_bindir}/vi

%patchlist
# Validate HTTP proxy status responses (CVE-2012-0804).
1001-fix-proxy-response-parser.patch
# Reject CVS roots beginning with an option (CVE-2017-12836).
1002-reject-leading-dash-in-cvsroot.patch
# Use literal format strings for hardened builds.
1003-fix-format-security.patch
# Use the system allocation declarations.
2000-use-system-stdlib-declarations.patch
# Avoid glibc's rejection of the writable %n probe.
2001-avoid-glibc-dynamic-percent-n.patch
# Accept the riscv64-openruyi-linux triplet.
2002-accept-riscv64-openruyi-triplet.patch
# Accept quoted getopt diagnostics in the tests.
2003-accept-quoted-getopt-diagnostics.patch
# Avoid fgrep deprecation warnings in the tests.
2004-use-grep-f-in-sanity-tests.patch
# Serialize the full local, remote, and proxy sanity suites.
2005-serialize-sanity-modes.patch
# Retain redirect targets so repeated responses are detected.
2006-retain-redirect-target-for-loop-detection.patch

%description
CVS is a version control system that records the history of files and
coordinates concurrent changes to hierarchical source trees. It supports
local repositories and remote access through secure shell transports.

%conf
# The default autotools macro passes --docdir, which this bundled configure
# rejects. Invoke it directly with the required installation paths instead.
# Select the bundled time/printf fallbacks for the legacy function checks.
# Its ptrdiff_t size probe finds no declaration (size 0); disabling the
# unique-type branch avoids a duplicate switch case on LP64.
ac_cv_func_nanotime=no \
ccvs_cv_unique_int_type_ptrdiff_t=no \
ac_cv_func_vasnprintf=no \
ac_cv_func_vasprintf=no \
CFLAGS="%{optflags} -std=gnu17 -D_GNU_SOURCE" LDFLAGS="%{build_ldflags}" ./configure \
    --build=%{_build} \
    --host=%{_host} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --with-editor=%{_bindir}/vi \
    --with-external-zlib \
    --with-rsh=%{_bindir}/ssh

%install -a
# These unsupported or obsolete helpers are outside the core CVS package.
rm -f %{buildroot}%{_bindir}/cvsbug
rm -f %{buildroot}%{_bindir}/rcs2log
rm -f %{buildroot}%{_mandir}/man8/cvsbug.8
rm -r %{buildroot}%{_datadir}/cvs
rm -f %{buildroot}%{_infodir}/dir

%files
%doc AUTHORS BUGS NEWS README
%license COPYING COPYING.LIB
%{_bindir}/cvs
%{_infodir}/cvs.info*
%{_infodir}/cvsclient.info*
%{_mandir}/man1/cvs.1*
%{_mandir}/man5/cvs.5*

%changelog
%autochangelog
