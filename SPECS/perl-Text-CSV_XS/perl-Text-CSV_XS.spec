# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-CSV_XS
Version:        1.62
Release:        %autorelease
Summary:        Comma-separated values manipulation routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-CSV_XS
#!RemoteAsset:  sha256:1710693eddaefdd56e74da42baa9ed676e7eaed28ebd303ad23c982fef2b1415
Source0:        https://www.cpan.org/authors/id/H/HM/HMBRAND/Text-CSV_XS-%{version}.tgz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
# perl already provides perl(Encode); standalone perl-Encode conflicts with perl.
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(XSLoader)

Requires:       perl(Encode) >= 3.22

%description
Text::CSV_XS provides facilities for the composition and decomposition of
comma-separated values. An instance of the Text::CSV_XS class will combine
fields into a CSV string and parse a CSV string into fields.

%files -f %{name}.files
%doc ChangeLog CONTRIBUTING.md LOVE_LETTER.md README SECURITY.md

%changelog
%autochangelog
