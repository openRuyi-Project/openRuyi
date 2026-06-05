# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Safe-Isa
Version:        1.000010
Release:        %autorelease
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Safe-Isa
#!RemoteAsset:  sha256:87f4148aa0ff1d5e652723322eab7dafa3801c967d6f91ac9147a3c467b8a66a
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)

Requires:       perl(Exporter) >= 5.57

%description
How many times have you found yourself writing:

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
