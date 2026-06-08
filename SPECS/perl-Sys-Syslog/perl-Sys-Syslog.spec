# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sys-Syslog
Version:        0.36
Release:        %autorelease
Summary:        Perl interface to the UNIX syslog(3) calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sys-Syslog
#!RemoteAsset:  sha256:ed42a9e5ba04ad4856cc0cb5d38d289c3c5d3764543ec04efafc4af7e3378df8
Source0:        https://www.cpan.org/authors/id/S/SA/SAPER/Sys-Syslog-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel

%description
Sys::Syslog is an interface to the UNIX syslog(3) program. Call syslog()
with a string priority and a list of printf() args just like syslog(3).

%files -f %{name}.files
%doc Changes README README.win32

%changelog
%autochangelog
