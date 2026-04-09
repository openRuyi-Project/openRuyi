# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Roman
Version:        3.5
Release:        %autorelease
Summary:        Allows conversion between Roman and Arabic algarisms
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Roman
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SY/SYP/Text-Roman-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(warnings)

%description
This package supports both conventional Roman algarisms (which range from 1
to 3999) and Milhar Romans, a variation which uses a bar across the
algarism to indicate multiplication by 1_000. For the purposes of this
module, acceptable syntax consists of an underscore suffixed to the
algarism e.g. IV_V = 4_005. The term Milhar apparently derives from the
Portuguese word for "thousands" and the range of this notation extends the
range of Roman numbers to 3999 * 1000 + 3999 = 4_002_999.

%prep
%setup -q -n Text-Roman-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes perlcritic.rc README weaver.ini

%changelog
%autochangelog
