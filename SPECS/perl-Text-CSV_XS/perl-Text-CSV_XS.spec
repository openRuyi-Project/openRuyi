# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-CSV_XS
Version:        1.61
Release:        %autorelease
Summary:        Comma-separated values manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-CSV_XS
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-%{version}.tgz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode) >= 3.21
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(XSLoader)

Requires:       perl(Encode) >= 3.21

%description
Text::CSV_XS provides facilities for the composition and decomposition of
comma-separated values. An instance of the Text::CSV_XS class will combine
fields into a CSV string and parse a CSV string into fields.

%prep
%setup -q -n Text-CSV_XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog CONTRIBUTING.md LOVE_LETTER.md README SECURITY.md

%changelog
%autochangelog
