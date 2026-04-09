# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sort-Versions
Version:        1.62
Release:        %autorelease
Summary:        Perl 5 module for sorting of revision-like numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sort-Versions
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/Sort-Versions-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the 'version numbers' that many shared library systems and
revision control packages use. This is quite useful if you are trying to
deal with shared libraries. It can also be applied to applications that
intersperse variable-width numeric fields within text. Other applications
can undoubtedly be found.

%prep
%setup -q -n Sort-Versions-%{version}

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
