# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-LibXML
Version:        2.0213
Release:        %autorelease
Summary:        Perl Binding for libxml2
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-LibXML
#!RemoteAsset:  sha256:2af21c5d61ac34ea26a5fabf15ba5a5841e648f7189db3e33b6f28b5489802ab
Source0:        https://www.cpan.org/authors/id/T/TO/TODDR/XML-LibXML-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(locale)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Alien::Base::Wrapper)
BuildRequires:  perl(Alien::Libxml2)
BuildRequires:  perl(XML::NamespaceSupport) >= 1.07
BuildRequires:  perl(XML::SAX) >= 0.11
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::DocumentLocator)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       perl(Exporter) >= 5.57
Requires:       perl(XML::NamespaceSupport) >= 1.07
Requires:       perl(XML::SAX) >= 0.11

%description
This module is an interface to libxml2, providing XML and HTML parsers with
DOM, SAX and XMLReader interfaces, a large subset of DOM Layer 3 interface
and a XML::XPath-like interface to XPath API of libxml2. The module is
split into several packages which are not described in this section; unless
stated otherwise, you only need to use XML::LibXML; in your programs.

%files -f %{name}.files
%doc AI_POLICY.md Changes HACKING.txt README.md

%changelog
%autochangelog
