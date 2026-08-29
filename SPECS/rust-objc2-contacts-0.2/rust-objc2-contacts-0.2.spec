# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-contacts
%global full_version 0.2.2
%global pkgname objc2-contacts-0.2

Name:           rust-objc2-contacts-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-contacts"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:a5ff520e9c33812fd374d8deecef01d4a840e7b41862d849513de77e44aa4889
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cnfetchrequest) = %{version}
Provides:       crate(%{pkgname}/contactsdefines) = %{version}

%description
Source code for takopackized Rust crate "objc2-contacts"

%package     -n %{name}+cnchangehistoryevent
Summary:        Bindings to the Contacts framework - feature "CNChangeHistoryEvent" and 11 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cnchangehistoryevent) = %{version}
Provides:       crate(%{pkgname}/cncontactproperty) = %{version}
Provides:       crate(%{pkgname}/cncontactrelation) = %{version}
Provides:       crate(%{pkgname}/cncontainer) = %{version}
Provides:       crate(%{pkgname}/cngroup) = %{version}
Provides:       crate(%{pkgname}/cninstantmessageaddress) = %{version}
Provides:       crate(%{pkgname}/cnlabeledvalue) = %{version}
Provides:       crate(%{pkgname}/cnmutablegroup) = %{version}
Provides:       crate(%{pkgname}/cnmutablepostaladdress) = %{version}
Provides:       crate(%{pkgname}/cnphonenumber) = %{version}
Provides:       crate(%{pkgname}/cnpostaladdress) = %{version}
Provides:       crate(%{pkgname}/cnsocialprofile) = %{version}

%description -n %{name}+cnchangehistoryevent
This metapackage enables feature "CNChangeHistoryEvent" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CNContactProperty", "CNContactRelation", "CNContainer", "CNGroup", "CNInstantMessageAddress", "CNLabeledValue", "CNMutableGroup", "CNMutablePostalAddress", "CNPhoneNumber", "CNPostalAddress", and "CNSocialProfile" features.

%package     -n %{name}+cnchangehistoryfetchrequest
Summary:        Bindings to the Contacts framework - feature "CNChangeHistoryFetchRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cnchangehistoryfetchrequest) = %{version}

%description -n %{name}+cnchangehistoryfetchrequest
This metapackage enables feature "CNChangeHistoryFetchRequest" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontact
Summary:        Bindings to the Contacts framework - feature "CNContact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscalendar) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cncontact) = %{version}

%description -n %{name}+cncontact
This metapackage enables feature "CNContact" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontactfetchrequest
Summary:        Bindings to the Contacts framework - feature "CNContactFetchRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Provides:       crate(%{pkgname}/cncontactfetchrequest) = %{version}

%description -n %{name}+cncontactfetchrequest
This metapackage enables feature "CNContactFetchRequest" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontactformatter
Summary:        Bindings to the Contacts framework - feature "CNContactFormatter" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsformatter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cncontactformatter) = %{version}
Provides:       crate(%{pkgname}/cnpostaladdressformatter) = %{version}

%description -n %{name}+cncontactformatter
This metapackage enables feature "CNContactFormatter" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CNPostalAddressFormatter" feature.

%package     -n %{name}+cncontactstore
Summary:        Bindings to the Contacts framework - feature "CNContactStore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cncontactstore) = %{version}

%description -n %{name}+cncontactstore
This metapackage enables feature "CNContactStore" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontactvcardserialization
Summary:        Bindings to the Contacts framework - feature "CNContactVCardSerialization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/cncontactvcardserialization) = %{version}

%description -n %{name}+cncontactvcardserialization
This metapackage enables feature "CNContactVCardSerialization" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontact-nsitemprovider
Summary:        Bindings to the Contacts framework - feature "CNContact_NSItemProvider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Provides:       crate(%{pkgname}/cncontact-nsitemprovider) = %{version}

%description -n %{name}+cncontact-nsitemprovider
This metapackage enables feature "CNContact_NSItemProvider" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cncontact-predicates
Summary:        Bindings to the Contacts framework - feature "CNContact_Predicates" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cncontact-predicates) = %{version}
Provides:       crate(%{pkgname}/cncontainer-predicates) = %{version}
Provides:       crate(%{pkgname}/cngroup-predicates) = %{version}

%description -n %{name}+cncontact-predicates
This metapackage enables feature "CNContact_Predicates" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CNContainer_Predicates", and "CNGroup_Predicates" features.

%package     -n %{name}+cncontactsuserdefaults
Summary:        Bindings to the Contacts framework - feature "CNContactsUserDefaults" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cncontactsuserdefaults) = %{version}
Provides:       crate(%{pkgname}/cnerror) = %{version}
Provides:       crate(%{pkgname}/cnsaverequest) = %{version}

%description -n %{name}+cncontactsuserdefaults
This metapackage enables feature "CNContactsUserDefaults" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CNError", and "CNSaveRequest" features.

%package     -n %{name}+cnfetchresult
Summary:        Bindings to the Contacts framework - feature "CNFetchResult"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Provides:       crate(%{pkgname}/cnfetchresult) = %{version}

%description -n %{name}+cnfetchresult
This metapackage enables feature "CNFetchResult" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cnmutablecontact
Summary:        Bindings to the Contacts framework - feature "CNMutableContact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscalendar) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cnmutablecontact) = %{version}

%description -n %{name}+cnmutablecontact
This metapackage enables feature "CNMutableContact" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the Contacts framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/cnchangehistoryevent) = %{version}
Requires:       crate(%{pkgname}/cnchangehistoryfetchrequest) = %{version}
Requires:       crate(%{pkgname}/cncontact) = %{version}
Requires:       crate(%{pkgname}/cncontact-nsitemprovider) = %{version}
Requires:       crate(%{pkgname}/cncontact-predicates) = %{version}
Requires:       crate(%{pkgname}/cncontactfetchrequest) = %{version}
Requires:       crate(%{pkgname}/cncontactformatter) = %{version}
Requires:       crate(%{pkgname}/cncontactproperty) = %{version}
Requires:       crate(%{pkgname}/cncontactrelation) = %{version}
Requires:       crate(%{pkgname}/cncontactstore) = %{version}
Requires:       crate(%{pkgname}/cncontactsuserdefaults) = %{version}
Requires:       crate(%{pkgname}/cncontactvcardserialization) = %{version}
Requires:       crate(%{pkgname}/cncontainer) = %{version}
Requires:       crate(%{pkgname}/cncontainer-predicates) = %{version}
Requires:       crate(%{pkgname}/cnerror) = %{version}
Requires:       crate(%{pkgname}/cnfetchrequest) = %{version}
Requires:       crate(%{pkgname}/cnfetchresult) = %{version}
Requires:       crate(%{pkgname}/cngroup) = %{version}
Requires:       crate(%{pkgname}/cngroup-predicates) = %{version}
Requires:       crate(%{pkgname}/cninstantmessageaddress) = %{version}
Requires:       crate(%{pkgname}/cnlabeledvalue) = %{version}
Requires:       crate(%{pkgname}/cnmutablecontact) = %{version}
Requires:       crate(%{pkgname}/cnmutablegroup) = %{version}
Requires:       crate(%{pkgname}/cnmutablepostaladdress) = %{version}
Requires:       crate(%{pkgname}/cnphonenumber) = %{version}
Requires:       crate(%{pkgname}/cnpostaladdress) = %{version}
Requires:       crate(%{pkgname}/cnpostaladdressformatter) = %{version}
Requires:       crate(%{pkgname}/cnsaverequest) = %{version}
Requires:       crate(%{pkgname}/cnsocialprofile) = %{version}
Requires:       crate(%{pkgname}/contactsdefines) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the Contacts framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the Contacts framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the Contacts framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-contacts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
