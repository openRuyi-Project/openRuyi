# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# If we want to enable gnulib, change this to 1
%bcond gnulib 0

Name:           psutils
Version:        2.10
Release:        %autorelease
Summary:        PostScript utilities
License:        GPL-3.0-or-later
URL:            https://github.com/rrthomas/%{name}
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(conf):  --disable-relocatable

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
%if %{with gnulib}
BuildRequires:  gnulib-devel
%endif
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  sed
BuildRequires:  libpaper
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Provides:       %{name}-perl = %{version}-%{release}

%description
Utilities for manipulating PostScript documents.
Page selection and rearrangement are supported, including arrangement into
signatures for booklet printing, and page merging for n-up printing.

%prep -a
%if %{with gnulib}
gnulib-tool --import --no-changelog relocatable-perl
%endif
autoreconf -fi

%files
%license COPYING
%doc README
%{_bindir}/epsffit
%{_bindir}/extractres
%{_bindir}/includeres
%{_bindir}/psbook
%{_bindir}/psjoin
%{_bindir}/psnup
%{_bindir}/psresize
%{_bindir}/psselect
%{_bindir}/pstops
%{_datadir}/%{name}
%{_mandir}/man1/epsffit.1*
%{_mandir}/man1/extractres.1*
%{_mandir}/man1/includeres.1*
%{_mandir}/man1/psbook.1*
%{_mandir}/man1/psjoin.1*
%{_mandir}/man1/psnup.1*
%{_mandir}/man1/psresize.1*
%{_mandir}/man1/psselect.1*
%{_mandir}/man1/pstops.1*
%{_mandir}/man1/psutils.1*

%changelog
%autochangelog
