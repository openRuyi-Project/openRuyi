# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define slapdrundir %{_rundir}/slapd

%global contrib_overlays addpartial allowed allop autogroup authzid datamorph lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace variant vc

Name:           openldap
Version:        2.7.2
Release:        %autorelease
Summary:        An implementation of the Lightweight Directory Access Protocol
License:        OLDAP-2.8
URL:            https://www.openldap.org
VCS:            git:https://git.openldap.org/openldap/openldap.git
#!RemoteAsset:  sha256:aad731aa22118ff327b9b4ddfc4b6f18ef9476586205da88a532e90940b523d2
Source0:        https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz
Source1:        slapd.service
Source2:        openldap.conf
Source3:        ldap-user.conf
Source4:        slapd-initial.ldif
Source5:        README.openruyi
BuildSystem:    autotools

BuildOption(conf):  --libexecdir=%{_libexecdir}
BuildOption(conf):  --localstatedir=%{slapdrundir}
BuildOption(conf):  --enable-wrappers=no
BuildOption(conf):  --enable-spasswd
BuildOption(conf):  --enable-modules
BuildOption(conf):  --enable-shared
BuildOption(conf):  --enable-dynamic
BuildOption(conf):  --with-tls=openssl
BuildOption(conf):  --with-cyrus-sasl
BuildOption(conf):  --with-systemd
BuildOption(conf):  --enable-crypt
BuildOption(conf):  --enable-ipv6=yes
BuildOption(conf):  --enable-dynacl
BuildOption(conf):  --enable-aci
BuildOption(conf):  --enable-ldap=mod
BuildOption(conf):  --enable-meta=mod
BuildOption(conf):  --enable-sock=mod
BuildOption(conf):  --enable-mdb=mod
BuildOption(conf):  --enable-relay=mod
BuildOption(conf):  --enable-overlays=mod
BuildOption(conf):  --enable-syncprov=mod
BuildOption(conf):  --enable-ppolicy=mod
BuildOption(conf):  --with-yielding-select
BuildOption(conf):  --with-argon2=libargon2
BuildOption(check):  SLAPD_DEBUG=0
BuildOption(install):  STRIP_OPTS=""

BuildRequires:  pkgconfig(libargon2)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  mandoc
BuildRequires:  libtool
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)

Requires(pre):  systemd-sysusers
Requires(pre):  systemd
%systemd_requires
Recommends:     cyrus-sasl

%patchlist
# Remove build timestamps; https://api.opensuse.org/public/source/openSUSE:Factory/openldap2/reproducible.patch?rev=b02b3f2b76ff3785b64f1d45167beb94
2000-reproducible.patch
# Use the configured runtime directory; https://api.opensuse.org/public/source/openSUSE:Factory/openldap2/0003-LDAPI-socket-location.dif?rev=b02b3f2b76ff3785b64f1d45167beb94
2001-ldapi-socket-location.patch
# Build position-independent executables; https://api.opensuse.org/public/source/openSUSE:Factory/openldap2/0005-pie-compile.dif?rev=b02b3f2b76ff3785b64f1d45167beb94
2002-pie-compile.patch
# Declare the attribute cleanup function; https://api.opensuse.org/public/source/openSUSE:Factory/openldap2/gcc14-v2.patch?rev=b02b3f2b76ff3785b64f1d45167beb94
2003-cloak-attribute-declaration.patch

%description
OpenLDAP is a client and server reference implementation of the
Lightweight Directory Access Protocol v3 (LDAPv3).

The server provides several database backends and overlays.

%package        back-sock
Summary:        OpenLDAP Socket backend
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}:/usr/share/man/man5/slapd-sock.5.gz

%description    back-sock
The OpenLDAP socket back-end allows you to handle LDAP requests and
results with an external process listening on a Unix domain socket.

%package        back-meta
Summary:        OpenLDAP Meta backend
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}:/usr/share/man/man5/slapd-meta.5.gz

%description    back-meta
The OpenLDAP Meta back-end is able to perform basic LDAP proxying with
respect to a set of remote LDAP servers. The information contained in
these servers can be presented as belonging to a single Directory
Information Tree (DIT).

%package     -n libldap-data
Summary:        Configuration file for system-wide defaults for all uses of libldap
BuildArch:      noarch

%description -n libldap-data
The subpackage contains a configuration file used to set system-wide defaults
to be applied with all usages of libldap.

%package        contrib
Summary:        OpenLDAP Contrib Modules
Requires:       %{name} = %{version}-%{release}

%description    contrib
Various overlays found in contrib/:
addpartial    Intercepts ADD requests, applies changes to existing entries
allop
allowed       Generates attributes indicating access rights
autogroup
authzid       implements RFC 3829 support
cloak
datamorph     store enumerated values and fixed size integers
denyop
lastbind      writes last bind timestamp to entry
noopsrch      handles no-op search control
pw-sha2       generates/validates SHA-2 password hashes
pw-pbkdf2     generates/validates PBKDF2 password hashes
smbk5pwd      generates Samba3 password hashes (heimdal krb disabled)
trace         traces overlay invocation
variant       allows attributes/values to be shared between several entries
vc            implements the verify credentials extended operation

%package        client
Summary:        OpenLDAP client utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    client
OpenLDAP client utilities such as ldapadd, ldapsearch, ldapmodify.

%package        devel
Summary:        Libraries, Header Files and Documentation for OpenLDAP
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     cyrus-sasl-devel

%description    devel
This package provides the OpenLDAP libraries, header files, and
documentation.

%package        static
Summary:        Static libraries for the OpenLDAP libraries
Requires:       cyrus-sasl-devel
Requires:       pkgconfig(openssl)
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This package provides the static versions of the OpenLDAP libraries
for development.

%build -p
make depend

%build -a
%set_build_flags
# Build selected contrib overlays
for SLAPO_NAME in %{contrib_overlays}
do
  make -C contrib/slapd-modules/${SLAPO_NAME} %{?_smp_mflags} libexecdir=%{_libexecdir}
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd %{?_smp_mflags} libexecdir=%{_libexecdir} DEFS="-DDO_SAMBA" HEIMDAL_LIB=""

%install -a
ln -sfn %{_libexecdir}/slapd %{buildroot}%{_sbindir}/slapd

# Install selected contrib overlays
for SLAPO_NAME in %{contrib_overlays}
do
  make -C contrib/slapd-modules/${SLAPO_NAME} DESTDIR=%{buildroot} mandir=%{_mandir} libexecdir=%{_libexecdir} install
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd DESTDIR=%{buildroot} mandir=%{_mandir} libexecdir=%{_libexecdir} DEFS="-DDO_SAMBA" HEIMDAL_LIB="" install
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/slapd.service
sed -i 's|@LIBEXECDIR@|%{_libexecdir}|g' %{buildroot}%{_unitdir}/slapd.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_datadir}/openldap/slapd-initial.ldif
install -d -m 0700 %{buildroot}%{_sharedstatedir}/ldap
chmod a+x %{buildroot}%{_libdir}/liblber.so*
chmod a+x %{buildroot}%{_libdir}/libldap.so*
install -D -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/openldap.conf
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/ldap-user.conf

# Remove upstream server examples; initialization uses the reviewed LDIF.
rm -f %{buildroot}%{_sysconfdir}/openldap/slapd.conf*

%define DOCDIR %{_defaultdocdir}/%{name}
# Install upstream documentation
install -d %{buildroot}%{DOCDIR}/adminguide \
           %{buildroot}%{DOCDIR}/images \
           %{buildroot}%{DOCDIR}/drafts
install -m 644 doc/guide/admin/*.html doc/guide/admin/*.png %{buildroot}%{DOCDIR}/adminguide
install -m 644 doc/guide/images/*.gif %{buildroot}%{DOCDIR}/images
install -m 644 doc/drafts/* %{buildroot}%{DOCDIR}/drafts
install -m 644 ANNOUNCEMENT COPYRIGHT README CHANGES %{buildroot}%{DOCDIR}
install -m 644 %{SOURCE5} %{buildroot}%{DOCDIR}/README.openruyi
sed -i -e 's|@LIBEXECDIR@|%{_libexecdir}|g' -e 's|@DATADIR@|%{_datadir}|g' %{buildroot}%{DOCDIR}/README.openruyi
rm -f %{buildroot}%{_sysconfdir}/openldap/schema/README
rm -f %{buildroot}%{_sysconfdir}/openldap/slapd.ldif*

rm -f %{buildroot}%{_libexecdir}/openldap/*.a
rm -f %{buildroot}%{_mandir}/man5/slapd-dnssrv.5
rm -f %{buildroot}%{_mandir}/man5/slapd-null.5
rm -f %{buildroot}%{_mandir}/man5/slapd-passwd.5

# Provide a libldap_r for backwards-compatibility with OpenLDAP < 2.5.
ln -fs libldap.so "%{buildroot}%{_libdir}/libldap_r.so"

%pre
%sysusers_create_package ldap-user.conf %SOURCE3
%tmpfiles_create_package %{name} %SOURCE2

%post
%systemd_post slapd.service

%preun
%systemd_preun slapd.service

%postun
%systemd_postun slapd.service

%files
%config %{_sysconfdir}/openldap/schema/*.schema
%config %{_sysconfdir}/openldap/schema/*.ldif
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%{_sbindir}/slap*
%{_libexecdir}/openldap/*
%exclude %{_libexecdir}/openldap/back_meta*
%exclude %{_libexecdir}/openldap/back_sock*
%{_libexecdir}/slapd
%{_unitdir}/slapd.service
%{_tmpfilesdir}/openldap.conf
%{_sysusersdir}/ldap-user.conf
%dir %attr(0700, ldap, ldap) %{_sharedstatedir}/ldap
%dir %{_datadir}/openldap
%{_datadir}/openldap/slapd-initial.ldif
%doc %{_mandir}/man8/sl*
%doc %{_mandir}/man8/lloadd.*
%doc %{_mandir}/man5/*
%exclude %{_mandir}/man5/slapd-sock.*
%exclude %{_mandir}/man5/slapd-meta.*
%exclude %{_mandir}/man5/ldap.conf*
%dir %{DOCDIR}
%doc %{DOCDIR}/ANNOUNCEMENT
%doc %{DOCDIR}/COPYRIGHT
%doc %{DOCDIR}/README*
%doc %{DOCDIR}/CHANGES
%doc %{DOCDIR}/drafts
%doc %{DOCDIR}/adminguide
%doc %{DOCDIR}/images
%license LICENSE
%{_libdir}/liblber.so.*
%{_libdir}/libldap.so.*

%files back-sock
%{_libexecdir}/openldap/back_sock*
%doc %{_mandir}/man5/slapd-sock.*

%files back-meta
%{_libexecdir}/openldap/back_meta*
%doc %{_mandir}/man5/slapd-meta.*

%files -n libldap-data
%config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%doc %{_mandir}/man5/ldap.conf*
%{_sysconfdir}/openldap/ldap.conf.default

%files contrib
%{_libexecdir}/openldap/addpartial.*
%{_libexecdir}/openldap/allop.*
%{_libexecdir}/openldap/allowed.*
%{_libexecdir}/openldap/authzid.*
%{_libexecdir}/openldap/autogroup.*
%{_libexecdir}/openldap/cloak.*
%{_libexecdir}/openldap/datamorph.*
%{_libexecdir}/openldap/denyop.*
%{_libexecdir}/openldap/lastbind.*
%{_libexecdir}/openldap/noopsrch.*
%{_libexecdir}/openldap/pw-pbkdf2.*
%{_libexecdir}/openldap/pw-sha2.*
%{_libexecdir}/openldap/smbk5pwd.*
%{_libexecdir}/openldap/trace.*
%{_libexecdir}/openldap/variant.*
%{_libexecdir}/openldap/vc.*

%files client
%doc %{_mandir}/man1/ldap*
%doc %{_mandir}/man5/ldif.*
%dir /etc/openldap
%{_bindir}/ldap*

%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*.h
%{_libdir}/liblber.so
%{_libdir}/libldap*.so
%{_libdir}/pkgconfig/lber.pc
%{_libdir}/pkgconfig/ldap.pc

%files static
%_libdir/liblber.a
%_libdir/libldap*.a

%changelog
%autochangelog
