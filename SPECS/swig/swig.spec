# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           swig
Version:        4.4.1
Release:        %autorelease
Summary:        Connects C/C++/Objective C to some high-level programming languages
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://www.swig.org/
VCS:            git:https://github.com/swig/swig.git
#!RemoteAsset
Source0:        http://downloads.sourceforge.net/project/swig/swig/swig-%{version}/swig-%{version}.tar.gz
Source1:        ccache-swig.sh
Source2:        ccache-swig.csh
BuildSystem:    autotools

# disable OCaml,php,tcl,java,octave
BuildOption(conf):  --without-ocaml
BuildOption(conf):  --with-python3=python3
BuildOption(conf):  --without-php
BuildOption(conf):  --with-perl5
BuildOption(conf):  --without-tcl
BuildOption(conf):  --without-java
BuildOption(conf):  --without-guile
BuildOption(check):  -j1

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(python3)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  sed
BuildRequires:  perl-devel
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(fields)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  boost-devel
# Need when Source/CParse/parser.y is patched
BuildRequires:  bison
BuildRequires:  pkgconfig(lua)

%description
Simplified Wrapper and Interface Generator (SWIG) is a software
development tool for connecting C, C++ and Objective C programs with a
variety of high-level programming languages. SWIG is used with different
types of target languages including common scripting languages such as
Javascript, Perl, PHP, Python, Tcl and Ruby. The list of supported
languages also includes non-scripting languages such as C#, D, Go language,
Java including Android, Lua, OCaml, Octave, Scilab and R. Also several
interpreted and compiled Scheme implementations (Guile, MzScheme/Racket)
are supported. SWIG is most commonly used to create high-level interpreted
or compiled programming environments, user interfaces, and as a tool for
testing and prototyping C/C++ software.

%package     -n ccache-swig
Summary:        Fast compiler cache
License:        GPL-2.0-or-later
Requires:       swig

%description -n ccache-swig
ccache-swig is a compiler cache. It speeds up re-compilation of C/C++/SWIG
code by caching previous compiles and detecting when the same compile is
being done again. ccache-swig is ccache plus support for SWIG.

%package     -n python-swig
Summary:        Python package metadata for SWIG
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch
Provides:       python3-swig
%python_provide python3-swig

%description -n python-swig
This package registers swig as installed for Python with pip for the
purpose of using "swig" in build-system.requires of a pyproject.toml file.

%prep -a
for all in CHANGES README; do
    iconv -f ISO88591 -t UTF8 < $all > $all.new
    touch -r $all $all.new
    mv -f $all.new $all
done

%conf -p
./autogen.sh

%install -p
make clean-examples

pushd Examples/
# We don't want to ship files below.
find -type f -name '*.dsp' -delete -print
find -type f -name '*.dsw' -delete -print

# Convert files to UNIX format
for all in `find . -type f -not -path "./test-suite/*"`; do
    dos2unix -k $all
    chmod -x $all
done
rm -rf test-suite
popd

# we don't manually generate man doc like what fedora did
# it's too complex

# Enable ccache-swig by default
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -dm 755 %{buildroot}%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d

# Add swig.gdb
mkdir -p %{buildroot}%{_datadir}/%{name}/gdb
install -pm 644 Tools/swig.gdb %{buildroot}%{_datadir}/%{name}/gdb

# Create python package metadata
mkdir -p %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info
echo "rpm" > %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info/INSTALLER
cat > %{buildroot}%{python3_sitelib}/swig-%{version}.dist-info/METADATA <<_EOF
Metadata-Version: 2.1
Name: swig
Version: %{version}
_EOF

%files
%{_bindir}/swig
%{_datadir}/swig
%license LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%doc ANNOUNCE CHANGES CHANGES.current
%doc COPYRIGHT README TODO

%files -n ccache-swig
%{_bindir}/ccache-swig
%config %{_sysconfdir}/profile.d/ccache-swig.*sh

%files -n python-swig
%{python3_sitelib}/swig-%{version}.dist-info/

%changelog
%autochangelog
