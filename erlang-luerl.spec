%global srcname luerl
# Erlang packages do not provide debug subpackages.
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    0.2
Release:    %mkrel 1

Group:      Development/Erlang

License:    ASL 2.0
Summary:    Lua in Erlang
URL:        https://github.com/rvirding/%{srcname}
Source0:    https://github.com/rvirding/%{srcname}/archive/v%{version}.tar.gz

BuildRequires: erlang-rebar


%description
An experimental implementation of Lua 5.2 written solely in pure Erlang.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE
%doc examples
%doc README.md
%doc src/NOTES
%{erlang_appdir}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 0.2-1.mga6
+ Revision: 1068037
- imported package erlang-luerl

