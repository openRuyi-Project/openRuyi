# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond ruby 0

Name:           rrdtool
Version:        1.9.0
Release:        %autorelease
Summary:        Round Robin Database Tool to store and display time-series data
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://oss.oetiker.ch/rrdtool
VCS:            git:https://github.com/oetiker/rrdtool-1.x
#!RemoteAsset:  sha256:5e65385e51f4a7c4b42aa09566396c20e7e1a0a30c272d569ed029a81656e56b
Source0:        https://github.com/oetiker/rrdtool-1.x/releases/download/v%{version}/rrdtool-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  intltool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  libtool
BuildRequires:  groff
BuildRequires:  gettext
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  systemd
BuildRequires:  sed
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl

Requires:       fonts-dejavu
%{?systemd_requires}

%patchlist
# bindings/ruby: pass include paths during build and install, create vendor_ruby dir
rrdtool-1.6.0-ruby-2-fix.patch
# rrd_gfx: improve grid fitting with proper rounding
rrdtool-zero_vs_nothing.patch
Fix-compatibility-with-Tcl-9.0.patch
correctly-link-ruby-bindings.patch

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%package        devel
Summary:        RRDtool header files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to build programs making
use of the library.

%package        help
Summary:        Help document files for %{name}
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}

%description    help
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package contains documentation on using RRD.

%package        perl
Summary:        Perl RRDtool bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl-%{name} = %{version}-%{release}
Obsoletes:      perl-%{name} < %{version}-%{release}

%description    perl
The Perl RRDtool bindings.

%package        -n python3-rrdtool
%{?python_provide:%python_provide python3-rrdtool}
Summary:        Python RRDtool bindings
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?__python3:Requires: %{__python3}}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-rrdtool
Python RRDtool bindings.

%package        tcl
Summary:        Tcl RRDtool bindings module
BuildRequires:  pkgconfig(tcl)
Requires:       tcl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       tcl-%{name} = %{version}-%{release}
Obsoletes:      tcl-%{name} < %{version}-%{release}

%description    tcl
The %{name}-tcl package includes RRDtool bindings for Tcl.

%if %{with ruby}
%{!?ruby_vendorarchdir: %global ruby_vendorarchdir %(ruby -rrbconfig -e 'puts Config::CONFIG["vendorarchdir"]')}

%package        ruby
Summary:        Ruby RRDtool bindings module
BuildRequires:  ruby
BuildRequires:  pkgconfig(ruby)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ruby
The %{name}-ruby package includes RRDtool bindings for Ruby.
%endif

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global luapkgdir %{_datadir}/lua/%{luaver}

%package        lua
Summary:        Lua RRDtool bindings module
BuildRequires:  lua
BuildRequires:  pkgconfig(lua)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    lua
The %{name}-lua package includes RRDtool bindings for Lua.

%prep
%autosetup -n %{name}-%{version} -p1

# Fix to find correct python dir on lib64
perl -pi -e 's|get_python_lib\(0,0,prefix|get_python_lib\(1,0,prefix|g' configure

# Most edits shouldn't be necessary when using --libdir, but
# w/o, some introduce hardcoded rpaths where they shouldn't
perl -pi.orig -e 's|/lib\b|/%{_lib}|g' configure Makefile.in # php4/configure php4/ltconfig*

# Perl 5.10 seems to not like long version strings, hack around it
perl -pi.orig -e 's|1.299907080300|1.29990708|' bindings/perl-shared/RRDs.pm bindings/perl-piped/RRDp.pm

# fix config files for php4 bindings
# workaround needed due to https://bugzilla.redhat.com/show_bug.cgi?id=211069
# cp -p /usr/lib/rpm/config.{guess,sub} php4/

%build
./bootstrap
%configure --with-perl-options='INSTALLDIRS="vendor"' --disable-rpath \
           --enable-tcl-site --with-tcllib=%{_libdir} --enable-python \
           --disable-ruby --disable-libdbi --disable-static --with-pic \
           --with-systemdsystemunitdir=%{_unitdir}

# Fix another rpath issue
perl -pi.orig -e 's|-Wl,--rpath -Wl,\$rp||g' bindings/perl-shared/Makefile.PL

# Remove Rpath from Ruby
perl -pi.orig -e 's|-Wl,--rpath -Wl,\$\(EPREFIX\)/lib||g' bindings/ruby/extconf.rb
sed -i 's|extconf.rb \\|extconf.rb --vendor \\|' bindings/Makefile

# Force RRDp bits where we want 'em, not sure yet why the
# --with-perl-options and --libdir don't take
pushd bindings/perl-piped/
perl Makefile.PL INSTALLDIRS=vendor
perl -pi.orig -e 's|/lib/perl|/%{_lib}/perl|g' Makefile
popd

make

# Fix @perl@ and @PERL@
find examples/ -type f -exec perl -pi -e 's|^#! \@perl\@|#!%{__perl}|gi' {} \;
find examples/ -name "*.pl" -exec perl -pi -e 's|\015||gi' {} \;

%install
export PYTHON=%{__python3}
%make_install PYTHON="$PYTHON"

mv %{buildroot}%{perl_vendorlib}/RRDp.pm %{buildroot}%{perl_vendorarch}/

install -d doc2/html doc2/txt
cp -a doc/*.txt doc2/txt/
cp -a doc/*.html doc2/html/

install -d doc3/html
mv doc2/html/RRD*.html doc3/html/

rm -f examples/Makefile* examples/*.in

find examples/ -type f -exec chmod 0644 {} \;

# Clean up the buildroot
rm -rf %{buildroot}%{perl_vendorlib}/leaktest.pl \
    %{buildroot}%{_docdir}/%{name}-* \
    %{buildroot}%{perl_vendorarch}/ntmake.pl \
    %{buildroot}%{perl_archlib}/perllocal.pod \
    %{buildroot}%{_datadir}/%{name}/examples \
    %{buildroot}%{perl_vendorarch}/auto/*/{.packlist,*.bs}

%find_lang %{name} --generate-subpackages

%check

%post
%systemd_post rrdcached.service rrdcached.socket

%preun
%systemd_post rrdcached.service rrdcached.socket

%postun
%systemd_post rrdcached.service rrdcached.socket

%files
%license LICENSE
%doc CONTRIBUTORS COPYRIGHT TODO NEWS CHANGES THREADS
%{_bindir}/*
%{_libdir}/*.so.*
%{_unitdir}/rrdcached.service
%{_unitdir}/rrdcached.socket
%{_datadir}/%{name}

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/librrd.pc

%files tcl
%doc bindings/tcl/README
%{_libdir}/tclrrd*.so
%{_libdir}/rrdtool/*.tcl

%if %{with ruby}
%files ruby
%doc bindings/ruby/README
%{ruby_vendorarchdir}/RRD.so
%endif

%files perl
%doc doc3/html
%{perl_vendorarch}/*.pm
%attr(0755,root,root) %{perl_vendorarch}/auto/RRDs/

%files lua
%doc bindings/lua/README
%{_libdir}/lua/%{luaver}/*

%files -n python3-rrdtool
%doc bindings/python/COPYING bindings/python/README.md
%{python3_sitearch}/rrdtool*.so
%{python3_sitearch}/rrdtool-*.egg-info

%files help
%doc examples doc2/html doc2/txt
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
