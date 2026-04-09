# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-HTML
Version:        1.004
Release:        %autorelease
Summary:        Open an HTML file with automatic charset detection
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-HTML
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/C/CJ/CJM/IO-HTML-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.10
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Encode) >= 2.10
Requires:       perl(Exporter) >= 5.57

%description
IO::HTML provides an easy way to open a file containing HTML while
automatically determining its encoding. It uses the HTML5 encoding sniffing
algorithm specified in section 8.2.2.2 of the draft standard.

%prep
%setup -q -n IO-HTML-%{version}

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
