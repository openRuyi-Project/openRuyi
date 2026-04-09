# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tarname Locale-gettext

Name:           perl-%{tarname}
Version:        1.07
Release:        %autorelease
Summary:        Interface to gettext family of functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-gettext
#!RemoteAsset
Source0:        https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/%{tarname}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(POSIX)
# Optional
BuildRequires:  perl(Encode)
# Tests:
BuildRequires:  perl(Test)
# Tests
BuildRequires:  glibc-locale-base

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

%conf
# No configure

%build -p
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%check
# Testsuite fails with LANG=C.UTF-8 and glibc >=2.42
LANG=en_US.UTF-8 %{__make} test

%files -f %{name}.files
%defattr(-,root,root,755)
%doc README

%changelog
%autochangelog
