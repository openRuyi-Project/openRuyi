# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Env-Path
Version:        0.19
Release:        %autorelease
Summary:        Advanced operations on path variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env-Path
#!RemoteAsset:  sha256:244bf093798832a7d841d9ee5b4b0e6b489996eef63541e505091aa34a9015e2
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSB/Env-Path-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)

%description
Env::Path presents an object-oriented interface to path variables, defined
as that subclass of environment variables which name an ordered list of
filesystem elements separated by a platform-standard separator

%prep
%setup -q -n Env-Path-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
