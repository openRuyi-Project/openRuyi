# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTML-Parser
Version:        3.85
Release:        %autorelease
Summary:        HTML parser class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Parser
#!RemoteAsset:  sha256:fd42ba6abe07241cf0ad57be246c3980065f683e4465e59b46af9efebc8e0c71
Source0:        https://www.cpan.org/authors/id/O/OA/OALDERS/HTML-Parser-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel

%description
Objects of the HTML::Parser class will recognize markup and separate it
from plain text (alias data content) in HTML documents. As different
kinds of markup and text are recognized, the corresponding event handlers
are invoked.

%files -f %{name}.files
%doc Changes eg entities.html hints mkhctype mkpfunc README TODO

%changelog
%autochangelog
