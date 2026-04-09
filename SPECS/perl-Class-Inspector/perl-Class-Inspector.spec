# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Class-Inspector
Version:        1.36
Release:        %autorelease
Summary:        Get information about a class and its structure
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Class-Inspector
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Class-Inspector-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Test::More) >= 0.98

Requires:       perl(File::Spec) >= 0.80

%description
Class::Inspector allows you to get information about a loaded class. Most
or all of this information can be found in other ways, but they aren't
always very friendly, and usually involve a relatively high level of Perl
wizardry, or strange and unusual looking code. Class::Inspector attempts to
provide an easier, more friendly interface to this information.

%prep
%setup -q -n Class-Inspector-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc author.yml Changes maint perlcriticrc README

%changelog
%autochangelog
