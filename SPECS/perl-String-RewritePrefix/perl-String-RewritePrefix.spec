# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-String-RewritePrefix
Version:        0.009
Release:        %autorelease
Summary:        String::RewritePrefix Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/String-RewritePrefix
#!RemoteAsset:  sha256:44918bec96a54af8ca37ca897e436709ec284a07b28516ef3cce4666869646d5
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/String-RewritePrefix-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Exporter) >= 0.972
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Sub::Exporter) >= 0.972

%description
String::RewritePrefix Perl module

%prep
%setup -q -n String-RewritePrefix-%{version}

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
