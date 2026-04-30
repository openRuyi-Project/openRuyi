# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-strictures
Version:        2.000006
Release:        %autorelease
Summary:        Turn on strict and make most warnings fatal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/strictures
#!RemoteAsset:  sha256:09d57974a6d1b2380c802870fed471108f51170da81458e2751859f2714f8d57
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/strictures-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
I've been writing the equivalent of this module at the top of my code for
about a year now. I figured it was time to make it shorter.

%prep
%setup -q -n strictures-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
%autochangelog
