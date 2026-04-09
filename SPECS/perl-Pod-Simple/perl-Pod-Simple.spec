# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Simple
Version:        3.47
Release:        %autorelease
Summary:        Framework for parsing Pod
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Simple
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/K/KH/KHW/Pod-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode) >= 2.78
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Escapes) >= 1.04
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Wrap) >= 98.112902
BuildRequires:  perl(warnings)

Requires:       perl(Encode) >= 2.78
Requires:       perl(Pod::Escapes) >= 1.04
Requires:       perl(Text::Wrap) >= 98.112902

%description
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules. The Pod format is explained in
perlpod; the most common formatter is called perldoc.

%prep
%setup -q -n Pod-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README

%changelog
%autochangelog
