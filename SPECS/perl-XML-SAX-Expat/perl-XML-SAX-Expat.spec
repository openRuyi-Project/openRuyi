# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-SAX-Expat
Version:        0.51
Release:        %autorelease
Summary:        SAX2 Driver for Expat (XML::Parser)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-SAX-Expat
#!RemoteAsset:  sha256:4c016213d0ce7db2c494e30086b59917b302db8c292dcd21f39deebd9780c83f
Source0:        https://www.cpan.org/authors/id/B/BJ/BJOERN/XML-SAX-Expat-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
BuildRequires:  perl(XML::Parser) >= 2.27
BuildRequires:  perl(XML::SAX) >= 0.03
BuildRequires:  perl(XML::SAX::Base) >= 1.00

Requires:       perl(XML::NamespaceSupport) >= 0.03
Requires:       perl(XML::Parser) >= 2.27
Requires:       perl(XML::SAX) >= 0.03
Requires:       perl(XML::SAX::Base) >= 1.00

%description
This is an implementation of a SAX2 driver sitting on top of Expat
(XML::Parser) which Ken MacLeod posted to perl-xml and which I have
updated.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
